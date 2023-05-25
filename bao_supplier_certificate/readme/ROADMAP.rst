- Disable the ability to create a certificate without a certificate
  generator. There should be only one flow to create a certificate.
- Make the certificate immutable. Certificates should not change after
  their creation. So remove "draft" state and keep the others.
