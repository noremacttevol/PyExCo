# Analogy Library

Master list of industrial/electrical analogies used to teach Python concepts. **Reuse these for consistency.** When introducing a new concept, check here first to see if an existing analogy fits before inventing a new one.

---

## Variables → Labeled Junction Boxes
A variable is a labeled junction box. The label is the name (`motor_speed`), the wires inside are the value (`1750`). You can swap out what's in the box, but the label stays.

## Data Types → Wire Gauges & Conductor Types
- `int` / `float` = current-carrying conductors (numbers do work)
- `str` = labels and tags (text describes things)
- `bool` = a contact: open (False) or closed (True)
- `list` = a multi-conductor cable — multiple values bundled together, accessed by position

## If/Elif/Else → Ladder Logic Rungs
Series of contacts on a rung. First True contact energizes the output. `else` is the default coil at the bottom.

## While Loop → A Latched Relay with a Stop Condition
Keeps running as long as the condition stays True. The "stop button" is what makes the condition flip to False. Without a stop condition, you've got a runaway motor — infinite loop.

## For Loop → A Conveyor Belt with a Counter
Each item on the belt gets processed in order. The loop runs once per item, then stops when the belt is empty.

## Functions → Pre-Built Motor Control Modules
A function is a sealed control module with inputs (parameters) and outputs (return values). You wire it up once, then call it whenever you need that operation. Don't rebuild a soft-start every time — call the module.

## Lists → Multi-Conductor Cable / Terminal Strip
A list is a terminal strip with numbered positions. Position 0 is terminal 1, position 1 is terminal 2, and so on (Python counts from zero — like landing wires starting at TB-0 instead of TB-1).

## Dictionaries → Labeled Terminal Block (Key/Value)
Instead of numbered positions, you have *named* terminals. Look up a value by its label, not its position. Like a panel where each terminal has a wire number printed on it: `panel["L1"]` gives you the L1 wire's data.

## Random Module → A Coin-Flip Relay or Pseudo-Random PLC Function
Generates an unpredictable value when you ask for one. Like a control system that simulates random load conditions for testing.

## Indentation → How Python Reads the Ladder
Indentation tells Python which lines belong to which rung. Drop the indent and Python loses the rung — it doesn't know what code goes with what condition.

## Comments (`#`) → As-Built Markups on a Print
Notes you leave for the next electrician (or future you). Python ignores them. They exist for the human reading the code.

## `print()` → A Pilot Light / Status Indicator
Shows you what's happening inside the program. Doesn't change anything — just lets you see the state.

## `input()` → An HMI Touchscreen Prompt
Asks the operator (user) for a value before continuing. Whatever they type comes in as a string — like reading raw data off the HMI before converting it to a usable number.

## Errors → Trip Codes / Fault Lights
Python error messages are fault codes. Read them from the bottom up — that's where the actual problem is. The traceback above is just the path the fault took to get there.

---

## Reserved for Future Concepts (Add as we go)
- Classes → ?
- Try/Except → Overload Protection / Fault Handling
- File I/O → Reading/Writing to a Logging Device
- Imports → Pulling a Module Off the Shelf
