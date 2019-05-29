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

## Application
The translator's main purpose is to contribute as an accessibility tool. With this application, one could easily translate braille to text and then be able to translate it to audio, for example. Also, it would work as a teaching device, helping children to learn braille in an easier way.

## Main objective


## Description of input images
Given the program's main objetive, the input images that will be used are going to be any picture of a text written in braille that a person could've taken from their phone. As for the tests during the period of the developing of the code, the images used are going to be retrieved manually from the internet, trying to represent the real scenario in the most reliable way possible. 

With that said, below there are two examples of possible input images. 

<center><en><strong>Picture 1:</strong> Example image of braille text #1</en></center>
![example image of braille text #1](https://raw.githubusercontent.com/lucasturci/BrailleTextTranslator/master/images/1.jpg) 

<center><en><strong>Picture 1:</strong> Example image of braille text #2</en></center>
![example image of braille text #1](https://raw.githubusercontent.com/lucasturci/BrailleTextTranslator/master/images/2.gif) 

## Description of steps

1\. Transform original image into binary matrix
- Point operation: Thresholding

2\. Remove noise
- Convolution using median filter

3\. Determine diameter D of a braille circle 
- It will be calculated as the median of the diamters of all the circles in the image plus a small Є

4\. Segment image into blocks
- Each block corresponds to a single letter
- The image will be segmented into a grid of cells with sizes 2·D X 3·D  

5\. For each block, determine which letter it represents 

6\. Insert corresponding letter on top of the block it represents
