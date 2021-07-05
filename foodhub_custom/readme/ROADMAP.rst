S'il y a plusieurs lignes avec le même produit sur le sale_order,
le rapport sera erroné:

En gros, si dans SO1234, on a
- ligne 1, produit A, quantité 2, prix 10€,
- ligne 2, produit A, quantité 3, prix 15€,

dans le delivery slip du picking, on aura
- ligne 1, produit A, quantité 2, prix 10€,
- ligne 2, produit A, quantité 2, prix 10€.

(le picking reste correct, c'est le rapport qui est erroné)

Pour réparer, il faudrait lier la ligne du picking à la ligne du sale order au moment de la création du picking. Aujourd'hui, c'est un champs calculé au moment de la lecture du record. Il retrouve le sale order par le champ "origin" (string).
Estimation: 4h.
