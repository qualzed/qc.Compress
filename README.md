# **.qc** (qualzed compressor)
____
My compression program does not compress very much, but in the future I will replenish its stock of bytes for stronger compression.
I strongly **do not recommend** you to use it as your main compressor, my program has bugs and files with a LARGE WEIGHT may not be compressed and most likely you will lose the original program.

## How does compression and decompression work in .qc?
____
It's simple, in "modules\sizeof\size.py" you will find "replacements", this list contains information with bytes that need to be replaced with what is needed. You can manually fill the list, in future updates I will fill it myself.
____
Below I have attached a GIF to demonstrate my compressor in action.
![qcompressor](https://github.com/user-attachments/assets/a7a79aa1-3a18-4924-96fb-500c45a4578f)
____

## What do I want to do?
I would rather try to somehow compress the file to zeros and ones, so that later I can rewrite them in the same way, I think the compression will be stronger this way, because it will be easier to decompress 0 and 1 than to make a long list. 
For example, if there is a repetition of seven ones and 3 zeros, then they can be compressed to two zeros and two ones, this is already 6 bytes less, and now imagine that there will be about 100-200 of them.
