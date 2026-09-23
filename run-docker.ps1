# Power shell script to run docker the CNN model
# Usage in switch statement default

# geting parameter
param([string]$task = "")

# this working directory (as if you did pwd in linux)
$wd = $PSScriptRoot

# each of the script commands
switch($task) {
    "build"     { 
        Write-Host "!!! Remember to have Docker Desktop open if error during build !!!"
        docker build -t cat-cnn $wd 
    }
    "run"       {docker run --rm -it -v "${wd}:/usr/cat-cnn" -w /usr/cat-cnn cat-cnn}
    "clean"     {docker rmi cat-cnn}
    "images"    {docker images}
    default     { 
        Write-Host "Usage: .\docker.ps1 <OPTION>" 
        Write-Host "OPTION can either be: " 
        Write-Host "    build  - builds docker image"
        Write-Host "    run    - run the docker image"
        Write-Host "    clean  - remove the docker image"
        Write-Host "    images - list currently made docker images"
    }
}