ICT401 Assessment 3 - Julianne Jamie Calma - 202571946

FILES
- engine.py: core GameEngine logic (no print/input)
- cli_app.py: terminal version
- gui_app.py: Tkinter graphical version
- easy.txt, medium.txt, hard.txt: external WORD|Hint data
- game_history.txt: completed games are appended here
- Ass3_Julianne_Jamie_Calma_202571946.docx/.pdf: evaluation report

HOW TO RUN
1. Install Python 3 on your computer if it is not already installed.
2. Keep ALL files in the same folder.
3. Open the folder in VS Code (or another Python editor).
4. Open a terminal in this folder.
5. CLI version: python cli_app.py
6. GUI version: python gui_app.py

SCREENSHOTS YOU MUST TAKE YOURSELF
1. Open one or more word files in the editor so WORD|Hint formatting is visible.
2. Play multiple completed games using BOTH CLI and GUI, then open game_history.txt and screenshot the appended rows.
3. CLI screenshot(s): show a game in progress; type a number such as 5 so the validation message appears; also capture a final win/loss state.
4. GUI screenshot(s): show the Tkinter window, visual A-Z keyboard, active game/lives, and a final win/loss state.
5. Put these screenshots into the marked placeholders in the report before final submission.

IMPORTANT FOR THE LIVE DEMO
Be able to explain:
- engine.py contains game rules and state only.
- cli_app.py uses print/input and imports GameEngine.
- gui_app.py uses tkinter and imports the SAME GameEngine.
- word data comes from external text files, not hardcoded Python lists.
- validate_letter rejects numbers, symbols, more than one character, and repeated guesses.
- save_history appends completed games to game_history.txt.
