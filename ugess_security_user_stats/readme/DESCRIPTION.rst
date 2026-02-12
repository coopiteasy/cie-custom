Security for UGESS specific to Stats profiles.

This module is intended to set a user which rights will be pretty
much restricted to some anonymized stats.

To be able to achieve that whithout using an external user,
which would have required developping portal views,
there is here a hack to resctrict the right of the internal users.

Therefore, it is mandatory to add another low level group to real interna users :
ugess_security_user_stats.group_user_all_non_private_contacts
