#include "version.h"
#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>


char* ios_get_version() {
  NSString *systemVersion = [[UIDevice currentDevice] systemVersion];
  return (char *) systemVersion.UTF8String;
}
