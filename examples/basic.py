from karboai import KarboAI

api = KarboAI()

communities = api.community.all()

print(communities)

feed = api.community.feed(
    community_id=17
)

print(feed)

featured = api.blogs.featured(
    community_id=17
)

print(featured)
