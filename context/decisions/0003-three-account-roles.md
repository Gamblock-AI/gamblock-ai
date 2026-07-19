# ADR-0003: Three authoritative account roles

- Status: accepted
- Date: 2026-07-20
- Context version: `2026-07-20.3`
- Classification: operational supporting feature

## Decision

Gamblock-AI has exactly three authoritative account roles: `user` (protected
student), `partner` (accountability partner), and `admin` (operational
administrator). Organization ownership and administration remain relation-level
membership roles (`owner`, `admin`, `member`, `viewer`) and are not account
roles.

The legacy operational roles `content_admin`, `model_release_operator`,
`support_operator`, `research_evaluator`, and `platform_admin` migrate to
`admin`. Legacy `organization_owner` and `organization_admin` account roles
migrate to `partner`. The migration is idempotent, revokes pending legacy
operator invitations, and rewrites the public support author marker from
`support_operator` to `admin`.

An admin has all operational capabilities, but this does not weaken the
privacy boundary: no role can access raw browsing inputs or private recovery
content. Recent authentication, verified-email gates, audit logging, support
claim ownership, self-ticket exclusion, and two-distinct-admin emergency
approval remain enforced.

New accounts are provisioned directly by an admin. The backend generates a
one-time temporary password, requires a password change before issuing a normal
session, leaves email unverified, and never permits role mutation after account
creation. Public registration and Google account creation remain limited to
`user` and `partner`.

## Consequences

- Website route/menu policy and backend authorization use the same three-role
  matrix; backend checks remain authoritative.
- Admins can use `/support` only as requesters for their own team tickets and
  `/admin` as queue workers; an admin cannot claim their own ticket.
- The Flutter client remains `user`-only but supports the forced first-login
  password change for an admin-provisioned student.
- Deployment must snapshot the database before startup applies the migration.
