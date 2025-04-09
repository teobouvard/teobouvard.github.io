---
date: '2020-04-21'
title: Freezenet
summary: Making Proof-of-Work more useful.
tags:
  - software
---

# FreezeNet

FreezeNet is an attempt at making Proof of Work more computationally useful than it currently is.
The idea is to replace [Hashcash](http://www.hashcash.org/)-like challenges with neural network training.
This is not a fully-implemented alternative but only a proof of concept which was presented for a Data Mining project at the University of Stavanger.
However, the results are encouraging so it seems worth sharing.
Pull requests, questions and criticism are welcome.

For more information, you can read the [paper explaining this project](https://raw.githubusercontent.com/teobouvard/freezenet/master/freezenet_paper.pdf) or take a look at [the slides presenting it](https://raw.githubusercontent.com/teobouvard/freezenet/master/freezenet_presentation.pdf).

## Simple API

You can apply a watermark to a model at any point.

```python
model = FreezeNet()

some_signature = Signature(b'Some block information', 4096)
another_signature = Signature(b'Some other block information', 4096)

some_signature.sign(model)

some_signature.verify(model)    # True
another_signature.verify(model) # False

another_signature.sign(model)

some_signature.verify(model)    # False
another_signature.verify(model) # True
```

You can also train a model with a watermark.

```python
model = FreezeNet()
some_signature = Signature(b'Some block information', 4096)
model.fit(x_train, y_train, **train_parameters, signature=some_signature)
some_signature.verify(model) # True
```

## Learning ability

{{< image src="learning_ability.png" alt="Learning ability of watermarked models" position="center" style="border-radius: 4px;" >}}

## Weak tampering resistance

{{< image src="weak_tampering.png" alt="Weak tampering resistance of watermarked models" position="center" style="border-radius: 4px;" >}}

## Strong tampering resistance

{{< image src="strong_tampering.png" alt="Strong tampering resistance of watermarked models" position="center" style="border-radius: 4px;" >}}

## Cite this work

```bibtex
@misc{freezenet20,
    author = "Téo Bouvard",
    title  = "Freezenet: Making proof-of-work more useful",
    url    = "https://github.com/teobouvard/freezenet"
}

```
