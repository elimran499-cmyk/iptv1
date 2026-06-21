import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Channel:
    name: str
    url: str
    group: str = ""
    tvg_name: str = ""
    tvg_id: str = ""
    tvg_logo: str = ""

    def to_m3u(self) -> str:
        attrs = f'tvg-id="{self.tvg_id}" tvg-name="{self.tvg_name}" tvg-logo="{self.tvg_logo}" group-title="{self.group}"'
        return f'#EXTINF:-1 {attrs},{self.name}\n{self.url}'


def parse(path: str) -> list[Channel]:
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    channels = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#EXTINF"):
            name_match = re.search(r",(.+)$", line)
            name = name_match.group(1).strip() if name_match else "Unknown"
            group = _attr(line, "group-title")
            tvg_name = _attr(line, "tvg-name")
            tvg_id = _attr(line, "tvg-id")
            tvg_logo = _attr(line, "tvg-logo")
            i += 1
            url = lines[i].strip() if i < len(lines) else ""
            if url and not url.startswith("#"):
                channels.append(Channel(name=name, url=url, group=group,
                                        tvg_name=tvg_name, tvg_id=tvg_id, tvg_logo=tvg_logo))
        i += 1
    return channels


def write(channels: list[Channel], path: str) -> None:
    lines = ["#EXTM3U"] + [ch.to_m3u() for ch in channels]
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def _attr(line: str, key: str) -> str:
    match = re.search(rf'{key}="([^"]*)"', line)
    return match.group(1) if match else ""
