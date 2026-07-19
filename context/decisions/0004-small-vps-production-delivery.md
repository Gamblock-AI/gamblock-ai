# ADR-0004: Small VPS production delivery

- Status: accepted
- Date: 2026-07-20
- Context version: `2026-07-20.4`
- Classification: operational supporting feature

## Decision

Gamblock-AI uses one Ubuntu VPS for the current small-project deployment. The
host runs PostgreSQL, the backend, the website, and Caddy in Docker. Caddy owns
automatic TLS for `gamblock-ai.com`, redirects `www.gamblock-ai.com` to the
apex, and proxies `api.gamblock-ai.com` to the backend. Cloudflare provides
proxied DNS with Full (strict) origin validation.

The owner explicitly selected a single `root` SSH account using password
authentication on port 22. No deploy user, SSH authentication keypair, or
custom port is introduced. The committed inventory pins the observed ED25519
host identity; UFW, fail2ban, unattended upgrades, Docker log rotation, and a
small swapfile reduce the operational risk of this deliberately simple setup.

Images are private GHCR packages. GitHub Actions builds them with its scoped
repository token, while the VPS uses a read-packages PAT stored only in
Ansible Vault. Backend and website workflows deploy over root/password SSH only
after an explicit repository variable enables deployment. Production Ansible
application deployment fails before remote mutation when the GHCR PAT or core
database/JWT/AES settings are absent. SMTP and WhatsApp are optional delivery
adapters: missing credentials disable their workflows without enabling demo
previews or blocking the rest of production startup.

Flutter CI keeps one mutable `latest` release per repository. Every successful
`main` commit replaces fixed-name development assets and clearly labeled
`production-debug` assets configured with the production API/site.
Signed production assets are created only when the production-release variable
is enabled and both platform signing inputs are available; unsigned artifacts
are never presented as signed.

## Consequences

- This is an operational choice for the present project size, not a target for
  horizontal scaling or high availability.
- The root/password choice increases credential impact. Host-key pinning and
  brute-force controls mitigate but do not remove that risk.
- Cloudflare API access, the GHCR pull PAT, and platform signing material
  remain explicit external readiness gates. SMTP and WhatsApp provider setup
  remain feature-readiness gaps rather than deployment gates.
- Google web login needs the apex Authorized JavaScript Origin. The current GIS
  callback does not require a web redirect URI or client secret. Windows uses
  a Desktop OAuth client with PKCE and a dynamic loopback redirect; Android
  needs its package/signing-certificate OAuth registrations.
