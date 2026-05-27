Here is the complete file containing everything (Windows + Android installation, usage examples, and original library functions) in one full text, ready to copy.

---

```markdown
# KarboAI - Official Python SDK

Official Python SDK for KarboAI APIs.

Developed by Hisoka.

---

## Installation

### Windows Installation

#### Install from GitHub

```bash
pip install git+https://github.com/Zaicock/KarboAI.git
```

Or install manually

```bash
git clone https://github.com/Zaicock/KarboAI.git
cd KarboAI
pip install .
```

Test installation

```bash
python -c "from Karboai import KarboAI; print('Success')"
```

---

Android Installation (Pydroid 3)

Note: Pydroid 3 does not include git. Install manually.

1. Download the project

Download the ZIP file from:
https://github.com/Zaicock/KarboAI

Extract it to a folder, for example:
/storage/emulated/0/400/Application/KarboAI-main

2. Open Terminal in Pydroid and navigate to the folder

```bash
cd /storage/emulated/0/400/Application/KarboAI-main
```

3. Install requests

```bash
pip install requests
```

4. Install the library locally

```bash
pip install .
```

5. Test the installation

```bash
python -c "from Karboai import KarboAI; print('Success')"
```

---

Usage Example

Important: The correct import is from Karboai import KarboAI (with capital K).

Create a file test.py:

```python
from karboai import KarboAI

api = KarboAI()

# Get all communities
communities = api.community.all()
print(communities)

# Get community feed
feed = api.community.feed(community_id=17)
print(feed)

# Get featured blogs
blogs = api.blogs.featured(community_id=17)
print(blogs)

# Get user info
user = api.user.get(user_id="12345", community_id="17")
print(user)

# Resolve username → user info
resolved = api.user.resolve("test_user")
print(resolved)
```

Run the script:

```bash
python test.py
```

---

Original Library Functions

Community APIs

Function Description
api.community.all() Returns all communities
api.community.feed(community_id) Returns feed of a specific community

Blogs APIs

Function Description
api.blogs.featured(community_id) Returns featured blogs for a community

General

Function / Attribute Description
KarboAI() Initialize the API client
api.community Access community-related endpoints
api.blogs Access blogs-related endpoints

---

Notes

· If you get an authentication error (401), the API may require an API key. Try:

```python
api = KarboAI(api_key="your_api_key_here")
```

· Explore available methods using:

```python
print(dir(api.community))
print(dir(api.user))
print(dir(api.blogs))
```

---

License

MIT

Author

Hisoka

```

---

Copy the entire block above and save it as `README.md` or `INSTALL.txt`. This file contains everything needed for both Windows and Android users.
