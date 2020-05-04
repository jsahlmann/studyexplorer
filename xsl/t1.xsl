<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match = "/">
  <html>
  <body>
  <h2>START</h2>
  <xsl:apply-templates/>
  <h2>END</h2>
  </body>
  </html>
</xsl:template>

<xsl:template match="id_info">
  <p>NCT ID: <xsl:value-of select="nct_id"/></p>
</xsl:template>

<xsl:template match="required_header">
  <p>URL: <xsl:value-of select="url"/></p>
</xsl:template>

<xsl:template match="brief_title">
</xsl:template>

<xsl:template match="sponsors">
</xsl:template>

<xsl:template match="source">
</xsl:template>

<xsl:template match="brief_summary">
</xsl:template>

<xsl:template match="detailed_description">
</xsl:template>

<xsl:template match="overall_status">
</xsl:template>

<xsl:template match="phase">
</xsl:template>

<xsl:template match="study_type">
</xsl:template>

<xsl:template match="has_expanded_access">
</xsl:template>

<xsl:template match="study_design_info">
</xsl:template>

<xsl:template match="condition">
</xsl:template>

<xsl:template match="intervention">
</xsl:template>

<xsl:template match="eligibility">
</xsl:template>

<xsl:template match="location">
</xsl:template>

<xsl:template match="location_countries">
</xsl:template>

<xsl:template match="verification_date">
</xsl:template>

<xsl:template match="study_first_submitted">
</xsl:template>

<xsl:template match="study_first_submitted_qc">
</xsl:template>

<xsl:template match="study_first_posted">
</xsl:template>

<xsl:template match="last_update_submitted">
</xsl:template>

<xsl:template match="last_update_submitted_qc">
</xsl:template>

<xsl:template match="last_update_posted">
</xsl:template>

<xsl:template match="keyword">
</xsl:template>

<xsl:template match="condition_browse">
  <xsl:for-each select="mesh_term">
    <p><xsl:value-of select="."/></p>
  </xsl:for-each>
</xsl:template>

<xsl:template match="intervention_browse">
</xsl:template>

</xsl:stylesheet> 