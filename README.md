# Braille to Text Translator

## Authors 
- Bárbara Côrtes e Souza (@barbaracortes)
- Lucas Fernandes Turci  (@lucasturci)

## Abstract
Given a picture containing a braille message, the application translates the message into text and outputs two items:
- the corresponding message in ascii; and
- the original image with the ascii characters above the braille symbols.

## Image processing techniques involved
The main image processing tasks that are going to be used are image segmentation and image enhancement to improve visualization quality allowing to recognize change of depth, texture patterns, etc.

## Aplication
The translator's main purpose is to contribute as an accessibility tool. With this application, one could easily translate braille to text and then be able to translate it to audio, for example. Also, it would work as a teaching device, helping children to learn braille in an easier way.

## Main objective

## Description of input images

## Description of steps

1\. Transform original image to binary matrix
- Point operation: Thresholding

2\. Remove noise
- Convolution using median filter

3\. Determine diameter $D$ of a braille circle 
- It will be calculated as the median of the diamters of all the circles in the image plus a small Є

4\. Segment image into blocks
- Each block corresponds to a single letter
- The image will be segmented into a grid of cells with sizes $2\timesD$ x $3\timesD$  

5\. For each block, determine which letter it represents 

6\. Insert corresponding letter on top of the block it represents
