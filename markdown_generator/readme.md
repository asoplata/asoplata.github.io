# markdown generator

Austin's usability notes:

- the old notebooks and not-fully-implemented code for ORCID->Bibtex->TSV->MD page pipeline are either in subfolders `archaic` or `deprecated`, since they do not fully work.

- Currently (20250103), the way I barely have it working to make the Publications pages is:
  1. Enter your conda env
  2. MANUALLY edit and check your `publications.tsv`. Note that MS Excel inserts non UTF8 chars, etc.
  3. Run `python publications.py`, which uses the TSV file to recreate the appropriate MD page files in `../_publications`.
     - I have commented out the code which formerly added duplicates of information being inserted into the MD files themselves (such as adding MD-file-body content providing a link to the citation).
     - Instead of adding extra content to the MD-file-body itself, you should probably make edits to the templating system that writes HTML from the MD-file-header contents, using the templating in `../_layouts`, `../_includes`, etc.

- The Talk templating has much less functionality than the publications, so it's probably easier to add content using `talks.py`.
