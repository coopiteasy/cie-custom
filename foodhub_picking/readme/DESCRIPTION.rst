- Sort picking operations by internal category and internal reference. 

Context : Increase the efficiency of picking by sorting products by location and priority. We cannot use "locations" because some products are of type Consumable and should stay this way : these are products that are received and sent on the same date, we don't want to manage stock on these products. 
So instead we sort by internal categories and by reference.

- Put the name of the SO in title, rather than the picking reference. Because this picking will be sent to the client, who only knows the reference of the SO. In principle this document should not be sent to the client, but here it's easier to only rely on one document. 
