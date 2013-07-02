BEGIN {
  count = 0;
}
/notroot/ {
  count++;
}
END {
  print count;
}
