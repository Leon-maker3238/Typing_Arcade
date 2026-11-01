**Windows quick start:** Double-click `START_GAME.bat`. The website runs at http://127.0.0.1:5002. Login username: `Leon_Admin`; password is the one you provided. Extract to a NEW folder so the old database does not interfere.

# Typing Arcade 1.0

A runnable **local development build** of Typing Arcade 1.0. It contains an arcade interface, 20 browser-canvas game modes, typing-to-unlock, coins, costumes, hacks, purchasable pranks, prank blocks/reflection, owner-set game durations, owner-approved memberships, communities, competition listings, announcements, leaderboards, and password changes.

## Quick start with your requested Owner login

On Windows, right-click `START_WINDOWS.ps1` and choose **Run with PowerShell**, or open PowerShell in this folder and run `powershell -ExecutionPolicy Bypass -File .\START_WINDOWS.ps1`. On macOS/Linux, run `bash START_MAC_LINUX.sh`. These launchers configure the Owner username and supplied password, and will rename an existing Owner account without deleting progress. They update the Owner password on each launch.

**Security:** The supplied credentials are included in these local launcher scripts, and the supplied secret key is short. Change them before sharing the files or putting the website online.

## Start

Install Python 3.10+ and run in this folder:

```bash
python -m pip install -r requirements.txt
```

Set an Owner account **before the first launch** (the password must be at least 10 characters):

**Windows PowerShell**
```powershell
$env:OWNER_USERNAME="king"
$env:OWNER_PASSWORD="choose-a-long-secret-password"
$env:SECRET_KEY="replace-with-a-long-random-secret"
python app.py
```

**macOS / Linux**
```bash
export OWNER_USERNAME=king
export OWNER_PASSWORD='choose-a-long-secret-password'
export SECRET_KEY='replace-with-a-long-random-secret'
python app.py
```

Visit **http://127.0.0.1:5002**. The Owner account is created once, when no Owner exists. Other players register, then wait for Owner approval.

## What works / important limitations

- 20 **distinct lightweight canvas game modes** are implemented, with individual objectives and controls. They are **not** twenty full, polished 3D games. Some are simplified prototypes; collision, movement, and scoring should be improved through playtesting.
- Member requests, Owner approval, coins, shop inventory, typing challenge unlocks, game rounds, score storage, communities, competition creation, announcements and prank inventories are stored in SQLite.
- The Owner can change game durations. A requested “unlimited” setting uses a ten-minute cap in this prototype for safety.
- Prank blocking and reflection transactions work. Visual prank effects are **not yet applied in other players' game canvases**. Reflected pranks cannot bounce infinitely.
- Community membership exists, but **community-vs-community score aggregation and prizes are not yet implemented**.
- Competitions can be scheduled and displayed, but **automatic prize distribution, eligibility enforcement, and fully verified leaderboards are not yet implemented**.
- Scores have simple server-side bounds, **not authoritative game simulation**; do not use for high-stakes competitive rankings.
- Guests can browse the games but cannot start rounds in this build.
- Assistants can block members through the API with a reason; a dedicated Assistant management screen is not yet included.
- Mobile touch movement buttons exist, but keyboard-intensive game modes work best with a physical keyboard.
- This is a **local prototype**, not an internet-hosted public website. Public deployment needs HTTPS, a stable secret key, production hosting, database migrations, monitoring, backups, stronger security, abuse prevention, moderation and further testing.
- The `arcade.db` file is created on first run. Back it up if you want to preserve local progress.

## Security

Passwords use Werkzeug password hashing; sessions are signed; Owner and Assistant permissions are checked server-side. Most state-changing endpoints use a CSRF token. This code has not received a professional security audit and is not ready for unrestricted public deployment.

## Version name

This project is named **Typing Arcade 1.0**, as requested.
