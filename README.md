# Participant Selector

Simple tool for choosing who's going to help in class today :)

## How to run

```bash
# Python setup
pyenv virtualenv $(cat .python-version) participants
pyenv activate participants

# Create data file based on sample
cp participants.json_sample participants.json_s

# Run the project
python participant_selector.py

```

## What's missing?

- [ ] Load candidates from .json file
- [ ] Add some delay before showing the result (for building tension)
- [ ] Save the selected candidates to file, to avoid repeating results before everyone can participate
- [ ] Print selected participant's name using ASCII art
    - https://pypi.org/project/pyfiglet/
- [ ] Add lint validation
- [ ] Add automated testing
- [ ] Create CI scripts for validating lint and tests
- [ ] Add lint to pre-commit
- [ ] Multi-language support

## License

[MIT License](LICENSE)


