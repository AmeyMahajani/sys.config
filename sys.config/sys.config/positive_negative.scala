def checkNumber(): Unit = {
  println("Enter a Number: ")
  val number = scala.io.StdIn.readInt()
  if (number > 0) {
    println(s"$number is Positive")
  } else if (number < 0) {
    println(s"$number is Negative")
  } else {
    println(s"$number is Zero")
  }
}