#!/usr/bin/env python
# coding: utf-8

# In[11]:


orcid = '0000-0002-1680-6936' # Fill your orcid here


# In[12]:


import requests


# We use the `/works` api to list all works related to the orcid. This gives a summary of all works, so citation information is not included. We collect the `put-code` of all works to retrieve the citation information later.

# In[13]:


response = requests.get('https://pub.orcid.org/v3.0/{}/works'.format(orcid),
                        headers={"Accept": "application/orcid+json" })
record = response.json()


# In[14]:


put_codes = []
for work in record['group']:
    put_code = work['work-summary'][0]['put-code']
    put_codes.append(put_code)
put_code = put_codes[0]


# We use the `/<orcid>/work/<put-code>` endpoint to retrieve the citation information for each record.

# In[15]:


citations = []
for put_code in put_codes:
    response = requests.get('https://pub.orcid.org/v3.0/{}/work/{}'.format(orcid, put_code),
                            headers={"Accept": "application/orcid+json" })
    work = response.json()
    if work['citation'] is not None:
        citations.append(work['citation']['citation-value'])


# In[ ]:


with open('pubs.bib', 'w') as bibfile:
    for citation in citations:
        bibfile.write(citation)
        bibfile.write('\n')


# In[ ]:




