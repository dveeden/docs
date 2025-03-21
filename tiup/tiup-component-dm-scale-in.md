---
title: tiup dm scale-in
summary: The tiup dm scale-in command is used to scale in the cluster by taking the service offline and removing the specified node from the cluster. The syntax is "tiup dm scale-in <cluster-name> [flags]". Options include -N, --force, and -h for specifying nodes, forcing removal of down nodes, and printing help information. The output is the log of scaling in.
---

# tiup dm scale-in

The `tiup dm scale-in` command is used to scale in the cluster. Scaling in the cluster means taking the service offline, which eventually removes the specified node from the cluster and deletes the remaining related files.

## Syntax

```shell
tiup dm scale-in <cluster-name> [flags]
```

`<cluster-name>`: the name of the cluster to operate on. If you forget the cluster name, you can check it with the [cluster list](/tiup/tiup-component-dm-list.md) command.

## Options

### -N, --node

- Specifies the nodes to be scaled in. If you need to scale in multiple nodes, split them by commas.
- Data type: `STRINGS`
- Default: no. This option is mandatory and the value must be not null.

### --force

- In some cases, some scale-in nodes in the cluster have been down, making it impossible to connect to the node through SSH for operation. At this time, you can use the `--force` option to remove these nodes from the cluster.
- Data type: `BOOLEAN`
- Default: false. If this option is not specified in the command, the specified nodes are not forcibly removed.

### -h, --help

- Prints the help information.
- Data type: `BOOLEAN`
- Default: false

## Output

The log of scaling in.
