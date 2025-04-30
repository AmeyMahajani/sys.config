def isPrimeNumber_v2(): Unit = {
  println("Enter a number: ")
  val num = scala.io.StdIn.readInt()
  var isPrime = true

  if (num < 2) {
    isPrime = false
  } else {
    for (i <- 2 until num) {
      if (num % i == 0) {
        isPrime = false
      }
    }
  }

  if (isPrime) {
    println(s"$num is prime")
  } else {
    println(s"$num is not prime")
  }
}
