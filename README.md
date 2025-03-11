# EEP135-Casimir-Funk

## Project Overview
College undergraduates like all of us at Berkeley face many constraints when it comes to eating a healthy diet. We often don't have the time, money, space, equipment, nor patience to prepare fully-formed, well-cooked meals from scratch. Additionally, many of us follow diets that change what a well-rounded meal may look like.

Trader Joe's is a popular grocer that many college students rely on for easy and affordable meals. Using a subset of Trader Joe's items, specifically novelty and pre-prepared items, excluding fresh produce, we aim to find the most affordable shopping list to satisfy the FDA's recommended dietary intakes for the following diets:

Vegetarian, vegan, omnivore, carnivore, keto, and allergen-friendly.

## Methods
We first affixed price data prices from the third-party price tracker traderjoesprices.com to the collection of Trader Joe's items the FDA includes in the FDC, which includes nutrition information.

We then created a function that filters this subset of items to fit various items, narrowing our possibility matrix.

Using a linear program, we then solved for the lowest-cost shopping list to meet the needs of males and females aged 19-30, representing the majority of college undergraduates.

## Files
