#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>


char* get_version() {
  NSString *systemVersion = [[UIDevice currentDevice] systemVersion];
  return (char*) systemVersion.UTF8String;
}
