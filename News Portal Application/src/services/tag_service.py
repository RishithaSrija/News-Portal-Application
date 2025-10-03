from dao.tag_dao import TagDAO
from models.tag import Tag

class TagService:
    def __init__(self):
        self.dao = TagDAO()

    def create_tag(self, name: str) -> Tag | None:
        return self.dao.create_tag(name)

    def get_all_tags(self) -> list[Tag]:
        return self.dao.get_all_tags()

    def get_tag_by_id(self, tag_id: str) -> Tag | None:
        return self.dao.get_tag_by_id(tag_id)

    def delete_tag(self, tag_id: str) -> bool:
        return self.dao.delete_tag(tag_id)
