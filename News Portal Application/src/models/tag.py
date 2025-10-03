class Tag:
    def __init__(self, tag_id: int, name: str):
        self.tag_id = tag_id
        self.name = name

    def __repr__(self):
        return f"<Tag id={self.tag_id} name={self.name}>"

    def to_dict(self):
        return {
            "tag_id": self.tag_id,
            "name": self.name,
        }
