# KarboAI

Official Python SDK for KarboAI APIs.

Developed by Hisoka.

---

# Installation

## Install from GitHub

```bash
pip install git+https://github.com/Zaicock/KarboAI.git
```

---

# Local Installation (Android / Pydroid 3)

## 1. Download Project

Download the project ZIP from GitHub and extract it.

Project structure:

```bash
├── karboai/
├── examples/
├── setup.py
├── requirements.txt
└── README.md
```

---

## 2. Install Pydroid 3

Download:

https://play.google.com/store/apps/details?id=ru.iiec.pydroid3

---

## 3. Install Required Package

Open Pydroid Terminal and run:

```bash
pip install requests
```

---

## 4. Go To Project Folder

Example:

```bash
cd /storage/emulated/0/Download/karboai
```

---

## 5. Install KarboAI Locally

```bash
pip install .
```

If installed successfully you will see:

```bash
Successfully installed karboai
```

---

# Usage Example

Create file:

```bash
test.py
```

Code:

```python
from karboai import KarboAI

api = KarboAI()

# Get all communities
communities = api.community.all()

print(communities)

# Get community feed
feed = api.community.feed(
    community_id=17
)

print(feed)

# Get featured blogs
blogs = api.blogs.featured(
    community_id=17
)

print(blogs)
```

Run:

```bash
python test.py
```

---

# Features

- Community APIs
- Blogs APIs
- Clean Structure
- Easy To Use
- Expandable
- Mobile Friendly

---

# Author

Hisoka

---

# License

MIT
