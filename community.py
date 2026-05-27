class CommunityAPI:
    def __init__(self, client):
        self.client = client

    def feed(self, community_id, limit=20, offset=0):
        return self.client.get(
            "/community/feed",
            params={
                "community_id": community_id,
                "limit": limit,
                "offset": offset
            }
        )

    def all(self, limit=50, offset=0):
        return self.client.get(
            "/community/all",
            params={
                "limit": limit,
                "offset": offset
            }
        )

    def by_slug(self, slug):
        return self.client.get(
            f"/community/by-slug/{slug}"
        )
