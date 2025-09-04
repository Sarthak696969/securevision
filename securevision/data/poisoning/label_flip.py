# Simple label flip for TinyGTSRB
def label_flip(target_label: int):
    def _flip(y: int) -> int:
        return target_label
    return _flip
