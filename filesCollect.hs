-- Copy specified files (for example, dotfiles) to a specified destination
-- directory. Verbosity can be "silent", "normal", "verbose", or "deafening".
-- usage: filesCollect.hs fileListPath destDir verbosity

import System.Directory ( doesFileExist
			, doesDirectoryExist
			)
import Distribution.Simple.Utils ( installDirectoryContents
				 , installOrdinaryFile
				 )
import Distribution.Verbosity
import System.FilePath.Posix ( splitPath
			     , joinPath
			     )
import System.Environment (getArgs)
import Control.Monad

copy :: Verbosity -> FilePath -> FilePath -> IO ()
copy verbosity destDir src = do
    isFile <- doesFileExist src
    isDir <- doesDirectoryExist src
    if isDir 
        then installDirectoryContents verbosity src destPath
        else if isFile 
            then installOrdinaryFile verbosity src destPath
            else error "Something's wrong. Really wrong."
    where destPath = joinPath [destDir, last (splitPath src)]


parseVerbosity :: String -> Verbosity
parseVerbosity "silent" = silent
parseVerbosity "normal" = normal
parseVerbosity "verbose" = verbose
parseVerbosity "deafening" = deafening
-- should make this Maybe, perhaps?

work :: FilePath -> FilePath -> Verbosity -> IO ()
work fileListPath destDir verbosity = do
    fileList <- fmap lines $ readFile fileListPath 
    mapM_ (copy verbosity destDir) fileList

main :: IO ()
main = do
    rawArgs <- getArgs
    case rawArgs of
        [fileListPath, destDir] -> work fileListPath destDir normal
        [fileListPath, destDir, verbosity] -> 
            work fileListPath destDir $ parseVerbosity verbosity
	_ -> putStrLn "Why?"
