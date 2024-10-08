# cs351-hw-4
HW4: Implementing an AVL Tree

I believe this has everything implemented, except it is missing a critical piece: there is no rotational functionality. 
I tried really hard to get it to work, but I was at a loss for hours. At some point, I decided that the deadline was 
too close to keep bothering at it, so I skipped it and added everything else. I believe I have designed the rest in
such a way that it should still be correct given a proper rotational implementation. I also updated some tests which
assumed certain values for nodes such that they would make sense in a context with no rotation (see 
test_avltree_deletes.py, and traversal checks). 

In summary, everything is implemented except for proper height and balance factor checks, and therefore tree balancing.
I have a foundation for them which obviously does not work, so I hope the attempt would have some value. Finally,
thank you so much for the deadline extension until Monday, and I'm sorry for the disappointing delivery.
