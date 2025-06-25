# Video-Game-Puzzles

A repository that houses video game puzzle solvers. Most solvers are command line tools. Available solvers will be individually documented in this README.md

---

## 📦 Available Solvers

### Destiny 2's Vesper's Host Ice Breaker Catalyst Access Override Puzzles 2 and 3

Destiny 2's Vesper's Host Dungeon brought back a popular exotic sniper rifle from Destiny 1, Ice Breaker. In addition to the return of Ice Breaker is its new catalyst, which can be acquired through a lengthy line of quests associated with the Vesper's Host Dungeon. A part of this quest line involves completing the Access Override Triumph. The first task in this triumph is relatively trivial (four unique digits 1-9 that sum to a target value), the next two are slightly more complex but with the help of this solver can be calculated in seconds.

The second Access Override puzzle requires four unique digits (1-9) that multiply to equal target. Not super tough to work out, but our goal here is to make this process way faster. 

The third and last Access Override puzzle requires two sets of four unique digits (1-9) such that when those sets are individually summed, their two sums can be multiplied to equal target. The most complex of the three puzzles solved with ease by this tool.

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/gsw2019/video-game-puzzles.git
cd video-game-puzzles
```

2. **Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the solvers from source (Python required):

```bash
python {solver_folder}/src/main.py
```

---

## 📌 TODOs / Planned Additions

- Skyrim restoration loop calculator

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/license/MIT).

See the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

Garret Wilson

[LinkedIn](https://www.linkedin.com/in/garretwilson-mcb-cs/) • [GitHub](https://github.com/gsw2019)
