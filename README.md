# AI Recommendation Logic

A lightweight hybrid recommendation system that combines content similarity and user preference signals to rank items.

## Project structure
- `Project_Report.pdf` — searchable, selectable-text project report
- `Source_Code/recommender.py` — recommendation engine
- `Tests/test_recommender.py` — automated unit tests
- `LICENSE` — MIT License

## Requirements
- Python 3.9+
- No third-party packages required

## Run the demo
```bash
python Source_Code/recommender.py
```

## Run tests
```bash
python -m unittest discover -s Tests -v
```

## How it works
The engine tokenizes item descriptions, calculates Jaccard similarity against a user's liked-item profile, combines similarity with a popularity score, excludes already-liked items, and returns the highest-ranked recommendations.

## Author / Submission
Submitted by: Harshvarden  
Organization: DecodeLabs  
Date: 31 October
