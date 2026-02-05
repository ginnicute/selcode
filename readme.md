<p align="center">
  <pre align="center">
                                      .oPYo.        8                    8
                                      8             8                    8
                                      `Yooo. .oPYo. 8 .oPYo. .oPYo. .oPYo8 .oPYo.
                                          `8 8oooo8 8 8    ' 8    8 8    8 8oooo8
                                            8 8.     8 8    . 8    8 8    8 8.
                                      `YooP' `Yooo' 8 `YooP' `YooP' `YooP' `Yooo'
                                      :.....::.....:..:.....::.....::.....::.....:
                                      ::::::::::::::::::::::::::::::::::::::::::::
                                      ::::::::by Ginnicute::::::::::::::::::::::::
                                      ::::::::::::::::::::::::::::::::::::::::::::
  </pre>
</p>


## Using
Generate 1 code:

```console
user@hostname:~$ selcode gen
```

Output: ```Ваш код-подтверждение: 753-129```

Generate `N` codes:

```console
user@hostname:~$ selcode gen -n 5
```

Output:
```
Ваш код-подтверждение: 360-643
Ваш код-подтверждение: 317-268
Ваш код-подтверждение: 887-556
Ваш код-подтверждение: 782-798
Ваш код-подтверждение: 498-176
```

Help info:
```console
user@hostname:~$ selcode -h
```
```txt
usage: selcode [-h] {gen} ...

.oPYo.        8                    8
8             8                    8
`Yooo. .oPYo. 8 .oPYo. .oPYo. .oPYo8 .oPYo.
    `8 8oooo8 8 8    ' 8    8 8    8 8oooo8
     8 8.     8 8    . 8    8 8    8 8.
`YooP' `Yooo' 8 `YooP' `YooP' `YooP' `Yooo'
:.....::.....:..:.....::.....::.....::.....:
::::::::::::::::::::::::::::::::::::::::::::
::::::::by Ginnicute::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::

generator verification codes for cliens.
    

positional arguments:
  {gen}       Available commads:
    gen       generate verification codes

options:
  -h, --help  show this help message and exit

  Using:
  selcode gen              generate 1 code
  selcode gen -n 5         generate N codes

```

## Installation

### Method 1: Install from source

1. Clone repository:
    ```bash
    git clone https://github.com/yourusername/selcode.git && cd selcode
    ```
2. Grant execute permissions to the file:
    ```bash
    chmod +x selcode.py
    ```
3. Place the file in a directory accessible from PATH:
    ```bash
    # install for all users:
    sudo cp selcode.py /usr/local/bin/selcode

    # for local insatll (only for current user):
    mkdir -p ~/.local/bin
    cp selcode.py ~/.local/bin/selcode
    ```
3.1 (if you chose a local installation)Add ~/.local/bin in PATH
    ```bash
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```

### Method 2: Install from Makefile(Recommend)
1. Clone:
    ```bash
    git clone https://github.com/ginnicute/selcode && cd selcode
    ```
2. Install:
    ```bash
    sudo make install
    ```
---
