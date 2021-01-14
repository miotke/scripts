// A short and simple script written in Swift to copy a file
// from one directory to another. This was used as test code
// for a different project but I wanted to save it as a reference 
// for later. 
// USAGE: swift copy_file.swift

import Foundation

let fileManager = FileManager()
let userName = NSUsername()

// Append a file name include extension to the end of source and destination
let source = "/Users/\(userName)/Desktop/"
let destination = "/Users/\(userName)/Desktop/"

do { 
    try fileManager.copyItem(atPath: source, toPath: destination)
    print("copy successful")
} catch { 
    print("Error: \(error.localizedDescription)")
}

