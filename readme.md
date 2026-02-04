# Game Recommender System - Cosine Similarity

Content-based recommendation engine for video games using cosine similarity metrics and feature-based matching.

---

## Overview

Game recommendation system that analyzes game features and ratings to suggest similar games to users. Uses cosine similarity algorithm to compute feature-based similarities between games, enabling personalized content recommendations.

---

## Algorithm

**Content-Based Filtering:**
- Game feature vectors (genre, developer, publisher, mechanics, etc.)
- Cosine similarity computation between feature vectors
- Recommendation ranking by similarity score
- Top-N game suggestions based on user preferences

**Cosine Similarity:**
- `similarity = (A · B) / (||A|| × ||B||)`
- Measures angular distance in feature space
- Robust to feature scaling
- Computationally efficient

---

## Project Structure

```
├── Main.py          # Recommendation engine implementation
├── games.csv        # Game dataset with features
├── ratings.csv      # User ratings and preferences
└── README.md
```

---

## Datasets

**games.csv:**
- Game ID, name, genre, developer, publisher
- Release date, price, features
- Metadata for similarity computation

**ratings.csv:**
- User ID, game ID, rating
- User preference history
- Feedback for evaluation

---

## Key Features

✓ Content-based recommendation algorithm  
✓ Cosine similarity for feature matching  
✓ CSV-based data handling  
✓ Scalable to larger datasets  
✓ Easy-to-understand implementation  

---

## Technologies

**Python Libraries:** pandas, numpy, scikit-learn  
**Algorithms:** Cosine similarity, vector normalization  
**Data Format:** CSV files

---

## Usage

```bash
python Main.py
```

Input: User preferences or game ID  
Output: Top-N recommended games with similarity scores

---

## Recommendation Approach

1. **Feature Extraction:** Convert game metadata to feature vectors
2. **Normalization:** Scale features to comparable ranges
3. **Similarity Computation:** Calculate cosine similarity for all game pairs
4. **Ranking:** Sort by similarity score (highest first)
5. **Filtering:** Return top-N recommendations

---

## Author

**Aroutin Nazarian**