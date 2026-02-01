# Git Submodule Setup

This project uses **pybind11** as a git submodule. This ensures that the exact version of pybind11 is maintained and shared across the repository.

## Initial Clone with Submodules

When cloning this repository for the first time, use the `--recursive` flag to automatically initialize and clone all submodules:

```bash
git clone --recursive https://github.com/<your-repo>/Pybind11Example.git
```

If you've already cloned the repository without the `--recursive` flag, initialize the submodules manually:

```bash
cd Pybind11Example
git submodule update --init --recursive
```

## Updating Submodules

To update all submodules to their latest commits from their respective repositories:

```bash
git submodule update --remote --recursive
```

To update a specific submodule:

```bash
cd ThirdPartyLib/pybind11
git pull origin master
cd ../..
```

## Checking Submodule Status

To see the status of all submodules:

```bash
git submodule status
```

## Building the Project

After cloning and initializing submodules, build the project:

```bash
mkdir -p build
cd build
cmake ..
make
```

The CMakeLists.txt is configured to use the pybind11 submodule at `ThirdPartyLib/pybind11`.

## Key Files

- **`.gitmodules`**: Contains the configuration for all submodules (at repository root)
- **`.gitignore`**: Configured to exclude build artifacts and virtual environments
- **`ThirdPartyLib/pybind11`**: Tracked as a submodule pointing to the official pybind11 repository

## Notes

- Submodule commits are pinned to specific versions. This ensures reproducible builds.
- When committing changes that update a submodule, the parent repository will track the new commit hash.
- Team members must be aware that they need to use `--recursive` when cloning or manually initialize submodules after cloning.
