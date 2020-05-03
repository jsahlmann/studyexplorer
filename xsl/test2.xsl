<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="clinical_study/id_info">
  <html>
  <body>
  <h2>Study presentation</h2>
    <p><xsl:value-of select="nct_id"/></p>
  <h2>Ende</h2>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet> 