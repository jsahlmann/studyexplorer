<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Study titles</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>NCI ID</th>
      <th>Brief Study Title</th>
    </tr>
    <tr>
      <td><xsl:value-of select="clinical_study/id_info/nct_id"/></td>
      <td><xsl:value-of select="clinical_study/brief_title"/></td>
    </tr>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet> 