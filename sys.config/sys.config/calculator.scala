def calculator(): Unit = {
  println("Enter first number: ")
  val num1 = scala.io.StdIn.readDouble()
  println(s"You entered first number: $num1")
  println("Enter second number: ")
  val num2 = scala.io.StdIn.readDouble()
  println(s"You entered second number: $num2")
  println("Enter an operation from the list [add, sub, mul, div]: ")
  val operation: String = scala.io.StdIn.readLine()
  println(s"You entered choice of operation: $operation")
  if (operation == "add") {
    println(s"Result: ${num1 + num2}")
  } else if (operation == "sub") {
    println(s"Result: ${num1 - num2}")
  } else if (operation == "mul") {
    println(s"Result: ${num1 * num2}")
  } else if (operation == "div") {
    if (num2 != 0) {
      println(s"Result: ${num1 / num2}")
    } else {
      println("Cannot divide by zero")
    }
  } else {
    println("Invalid operation")
  }
}
