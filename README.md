# JES
Javascript enhanced subset

This project is born from my frustration with Javascript's syntax and semantics.
The result is a subset of what I consider as "the good parts" of Javascript, enhanced with syntactic sugar.

The current syntax is inspired by languages like Python, Golang, Rust, JS itself and probably some others that I forgot.

In order for this simple compiler to be reusable as learning material, I split the project into distinct parts.

As most compiler, this project follows the following scheme:

source code -> parse -> syntactic tree -> transform -> semantic tree -> write -> compiled code


## Syntax

```
// static bindings (const)
let x = 5

// mutable variables
let mut x = 5
```

```
// conditions
if x >= 5 {
    console.log(x)
} elif x < 5 {
    console.log(x)
}

// loops
while i <= n {
    i += 1 // increment syntax
}

// this part is not important for now
do {
    i -= 1
} while i > 0
```

```
// for loops
for x in [1, 2, 3] {
    console.log(x)
}
```

```
// functions
fn f(x, y, *args) {
    return x + y
}
// callbacks
fn () {
    return 1
}
```

```
// data types
// the runtime types are left untouched
// the object literal syntax follows the Python dictionary syntax,
// because it is easier to implement (not for my own preference)

let array = [1, 2, 3,]
let object = {
    key: value,
}
object.attribute = value

```

### Delayed features

These are just notes for myself until a prototype is complete.

#### Classes
Classes should be kept mostly as-is.

#### Modules
The user should be able to choose between Python-style modules and no module system at all.

#### Generators
#### Async/Await



