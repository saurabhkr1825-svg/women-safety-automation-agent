# Women Safety Automation Agent

Women Safety Automation Agent is an AI-based Android automation script that opens SOS apps, shares location, sends alerts, and prepares emergency calls from a single trigger to speed up help in critical situations.[web:69]

## Project Structure

- `main/` – Entry Python script(s) to start the agent.
- `agent/` – Agent configuration and logic (goals, orchestration).
- `actions/` – Reusable action modules (open apps, share location, send messages).
- `triggers/` – Trigger logic (how the flow is started, e.g. command or shortcut).
- `adb_sos/` – ADB or device-specific helpers for SOS and emergency actions.
- `droidrun_env/` – Environment/config files used by Droidrun (do not edit during demo).

## Requirements

- Python 3.10–3.12
- Android device or emulator with USB debugging enabled
- `pip` and `adb` installed
- Droidrun and an LLM provider (e.g. OpenAI API)

Install dependencies:

```bash
pip install droidrun
