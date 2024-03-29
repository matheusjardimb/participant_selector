# Participant Selector

Simple tool for choosing who's going to help in class today :)

## How to run

```bash
# Python setup
pyenv virtualenv $(cat .python-version) participants
pyenv activate participants

pip install -r requirements.txt
pre-commit install

# Create data file based on sample
cp participants.json_sample participants.json_s

# Run the project
python participant_selector.py

```

## What's missing?

- [x] Load candidates from .json file
- [x] Save the selected candidates to file
- [x] Print selected participant's name using ASCII art
- [x] Add lint validation
- [x] Add lint to pre-commit
- [x] Avoid repeating results before everyone can participate
- [ ] Add some delay before showing the result (for building tension)
- [ ] Add automated testing
- [ ] Create CI scripts for validating lint and tests
- [ ] Multi-language support

## License

[MIT License](LICENSE)
