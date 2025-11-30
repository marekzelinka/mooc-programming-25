# MOOC Programming 2025

All exercises for Introduction to Programming & Advanced Course in Programming courses from University of Helsinki, Finland.

## Setup

Install the [`tmc` cli tool](https://github.com/marekzelinka/mooc-programming-25):

On Linux run:

```sh
curl -0 https://raw.githubusercontent.com/rage/tmc-cli-rust/main/scripts/install.sh | bash -s x86_64 linux
```

Then login with your MOOC account:

```sh
tmc login # interactive guide
```

[Here is a guide](https://www.mooc.fi/en/installation/vscode) to setting up a [MOOC](https://www.mooc.fi/) account and the VSCode plugin.

## Usage

### Auth

#### Logging out

```sh
tmc logout
```

### Courses

#### Listing courses

```sh
tmc courses
```

#### Downloading course exercises (interactive)

```sh
tmc download
```

### Tests

#### Running tests (interactive)

```sh
tmc test
```

#### Submit (interactive)

```sh
tmc submit
```
