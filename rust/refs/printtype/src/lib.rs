#![feature(core_intrinsics)]

fn print_type_name_of<T>(_: T) {
    println!("{}", std::intrinsics::type_name::<T>())
}

#[test]
fn lvalue() {
    let x = &false;
    print_type_name_of(x);
}

#[test]
fn value() {
    let &x = &false;
    print_type_name_of(x);
}

#[test]
fn rvalue() {
    let ref x = &false;
    print_type_name_of(x);
}
