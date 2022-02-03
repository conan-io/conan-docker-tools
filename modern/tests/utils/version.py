from dataclasses import dataclass

@dataclass
class Version:
    full_version: str
    major: str
    minor: str = None
    patch: str = None

    def __init__(self, full_version=None):
        if not full_version:
            return

        self.full_version = full_version
        self.major, *rest = self.full_version.split('.', 1)
        if rest:
            self.minor, *rest = rest[0].split('.', 1)
            if rest:
                self.patch = rest[0]

    def __str__(self):
        ret = f"{self.major}"
        if self.minor is not None:
            ret += f".{self.minor}"
        if self.patch is not None:
            ret += f".{self.patch}"
        return ret

    def __lt__(self, other):
        return self.lazy_lt_semver(other)

    def lazy_lt_semver(self, other):
        lv1 = [int(v) for v in self.full_version.split(".")]
        lv2 = [int(v) for v in other.full_version.split(".")]
        min_length = min(len(lv1), len(lv2))
        return lv1[:min_length] < lv2[:min_length]
