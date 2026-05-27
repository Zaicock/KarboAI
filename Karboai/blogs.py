class BlogsAPI:
    def __init__(self, client):
        self.client = client

    def featured(self, community_id, limit=5):
        return self.client.get(
            "/blogs/featured",
            params={
                "community_id": community_id,
                "limit": limit
            }
        )

    def previously_featured(
        self,
        community_id,
        limit=6,
        offset=0
    ):
        return self.client.get(
            "/blogs/previously-featured",
            params={
                "community_id": community_id,
                "limit": limit,
                "offset": offset
            }
        )
