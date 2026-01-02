# How We Tried to Help a Farmer Buy Better Cows

## The Problem

A dairy farmer came to us with a simple question: "I'm about to buy 20 new cows. How do I know which ones will actually be worth the money?"

Fair question. Buying a cow is a gamble. The seller shows you a healthy animal, quotes some numbers, and you hope for the best. Six months later you find out the milk tastes off, or the yield is half of what you expected. By then, it's too late.

The farmer wanted something better than gut feeling. He had data on his current herd - 600+ cows with records on milk production, feed, breeding history, and taste ratings. Could we use that to predict how new cows would perform?

## What We Set Out to Build

Two models, working together:

1. **Yield prediction** - How much milk will this cow produce per year?
2. **Quality prediction** - Will the milk taste good?

A cow passes the test only if she hits both targets: at least 6,000 kg annually AND tasty milk.

## What Actually Happened

**The quality model worked.** We found that milk taste depends heavily on fat content, protein levels, and breed. The model picks up on these patterns and can flag cows likely to produce bad-tasting milk before you buy them.

**The yield model didn't.** This was the frustrating part. We threw everything at it - breed, father's breed, feed composition, pasture type, age. The model learned the training data perfectly but failed completely on new cows. Negative R-squared on the test set, meaning you'd be better off just guessing the herd average.

Why? Probably because the real drivers of milk yield aren't in the data we have. Genetics matter, but we only have breed names, not actual genetic markers. Feed matters, but we're missing seasonal variations. The father's breed is recorded, but not his actual milk production history.

## What the Farmer Can Do Now

**Use the quality model.** Before buying any cow, run her numbers through the model. If it says the milk will taste bad - walk away. This alone saves money.

**Assess yield the old way.** Until we get better data, stick with what works: look at the breed, check the age, ask about feeding history. It's not perfect, but it's honest.

**Start collecting better data.** Every cow you buy from now on - track her actual yield, month by month. In a year or two, we'll have enough information to build a yield model that actually works.

## The Honest Truth

We delivered half of what we promised. The quality prediction is solid and ready to use. The yield prediction needs more work and better data before it's useful.

That's not failure - that's how real projects go. You try something, see what works, and improve from there.

---

*Arina Fedorova*
