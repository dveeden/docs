---
title: Security Compatibility with MySQL
summary: Learn TiDB's security compatibilities with MySQL.
aliases: ['/docs/dev/security-compatibility-with-mysql/','/docs/dev/reference/security/compatibility/']
---

# Security Compatibility with MySQL

TiDB supports similar security functionality to MySQL 5.7, with the following exceptions:

- Column level permissions are not supported
- Password expiry, as well as password last-changed tracking and password lifetime are not supported [#9709](https://github.com/pingcap/tidb/issues/9709)
- The permission attributes `max_questions`, `max_updated`, `max_connections`, `max_user_connections` are not supported
- Password validation is not currently supported [#9741](https://github.com/pingcap/tidb/issues/9741)

## Authentication plugin status

Authentication in TiDB supports multiple authentication methods. The authentication method can be specified on a per user basis with [`CREATE USER`](/sql-statements/sql-statement-create-user.md) and [`ALTER USER`](/sql-statements/sql-statement-create-user.md). These authentication methods are compatible with the authentication methods of MySQL with the same name.

The default authentication method the server advertises during connection establishment can be set with the [`default_authentication_format`](/system-variables.md#default_authentication_format).

| Authentication Method    | Supported        |
| :------------------------| :--------------- |
| `mysql_native_password`  | Yes              |
| `sha256_password`        | No               |
| `caching_sha2_password`  | Yes, since 5.2.0 |
| `auth_socket`            | No               |
| TLS Certificates         | Yes              |
| LDAP                     | No               |
| PAM                      | No               |
| ed25519 (MariaDB)        | No               |
| GSSAPI (MariaDB)         | No               |
